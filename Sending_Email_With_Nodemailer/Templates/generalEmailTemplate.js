// Genel email template
function createEmailTemplate(data) {
    // Email tipini otomatik belirle
    const isQuestion = data.message && (
      data.message.includes('?') || 
      data.message.toLowerCase().includes('soru') ||
      data.message.toLowerCase().includes('nasıl') ||
      data.message.toLowerCase().includes('ne zaman') ||
      data.message.toLowerCase().includes('nerede')
    );
  
    const emailType = data.type || (isQuestion ? 'question' : 'info');
    
    // Tip ayarları
    const typeSettings = {
      question: { icon: '❓', color: '#3498db', bgColor: '#e8f4fd' },
      info: { icon: '📢', color: '#27ae60', bgColor: '#e8f5e8' },
      urgent: { icon: '🚨', color: '#e74c3c', bgColor: '#fdf2f2' },
      business: { icon: '💼', color: '#8e44ad', bgColor: '#f4f1f8' }
    };
  
    const settings = typeSettings[emailType] || typeSettings.info;
  
    const html = `
      <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; background: white;">
        <!-- Header -->
        <div style="background: ${settings.color}; padding: 30px 20px; text-align: center; color: white;">
          <h1 style="margin: 0; font-size: 24px;">
            ${settings.icon} ${data.title || 'Mesaj'}
          </h1>
          <p style="margin: 5px 0 0 0; opacity: 0.9; font-size: 14px;">
            ${new Date().toLocaleDateString('tr-TR')}
          </p>
        </div>
  
        <!-- Content -->
        <div style="padding: 30px 20px;">
          <!-- Greeting -->
          <h2 style="color: #333; margin: 0 0 15px 0; font-size: 18px;">
            ${data.greeting || `Merhaba ${data.recipientName || 'Değerli İlgili'},`}
          </h2>
  
          <!-- Main Message -->
          <div style="background: ${settings.bgColor}; padding: 20px; margin: 20px 0; border-radius: 8px; border-left: 4px solid ${settings.color};">
            <div style="color: #333; line-height: 1.6; font-size: 16px;">
              ${data.message || 'Mesaj içeriği belirtilmemiş.'}
            </div>
          </div>
  
          <!-- Additional Info -->
          ${data.additionalInfo ? `
          <div style="background: #f8f9fa; padding: 20px; margin: 20px 0; border-radius: 6px;">
            <h3 style="color: #333; margin: 0 0 10px 0; font-size: 16px;">📝 Ek Bilgiler:</h3>
            <div style="color: #666; line-height: 1.6;">
              ${data.additionalInfo}
            </div>
          </div>` : ''}
  
          <!-- Action Button -->
          ${data.actionUrl ? `
          <div style="text-align: center; margin: 30px 0;">
            <a href="${data.actionUrl}" 
               style="background: ${settings.color}; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; display: inline-block; font-weight: 500;">
              ${data.actionText || 'Tıklayın'}
            </a>
          </div>` : ''}
  
          <!-- Contact Info -->
          ${data.contactInfo ? `
          <div style="background: #f1f1f1; padding: 15px; margin: 20px 0; border-radius: 6px;">
            <h3 style="color: #333; margin: 0 0 10px 0; font-size: 14px;">📞 İletişim:</h3>
            <div style="color: #666; font-size: 14px;">
              ${data.contactInfo}
            </div>
          </div>` : ''}
  
          <!-- Closing -->
          <div style="margin-top: 30px; padding-top: 20px; border-top: 2px solid #eee;">
            <p style="color: #666; margin: 0; line-height: 1.5;">
              ${data.closing || (isQuestion ? 'Yanıtınızı bekliyorum.' : 'Bilgilerinize sunarım.')}
            </p>
            <p style="color: #333; margin: 10px 0 0 0; font-weight: 600;">
              ${data.senderName || process.env.FROM_NAME || 'Email Service'}
            </p>
          </div>
        </div>
  
        <!-- Footer -->
        <div style="background: #333; padding: 15px; text-align: center;">
          <p style="color: #999; margin: 0; font-size: 12px;">
            ${new Date().toLocaleString('tr-TR')} tarihinde gönderildi
          </p>
        </div>
      </div>
    `;
  
    const text = `
  ${data.title || 'Mesaj'}
  
  ${data.greeting || `Merhaba ${data.recipientName || 'Değerli İlgili'},`}
  
  ${data.message || 'Mesaj içeriği belirtilmemiş.'}
  
  ${data.additionalInfo ? `\n--- Ek Bilgiler ---\n${data.additionalInfo}\n` : ''}
  
  ${data.actionUrl ? `\nLink: ${data.actionUrl}\n` : ''}
  
  ${data.contactInfo ? `\n--- İletişim ---\n${data.contactInfo}\n` : ''}
  
  ${data.closing || (isQuestion ? 'Yanıtınızı bekliyorum.' : 'Bilgilerinize sunarım.')}
  
  ${data.senderName || process.env.FROM_NAME || 'Email Service'}
    `;
  
    return {
      subject: data.subject || `${settings.icon} ${data.title || 'Mesaj'}`,
      html: html,
      text: text
    };
  }
  
  module.exports = { createEmailTemplate };