import { http } from './http'

export const recommendationApi = {
  list: (memberId, origin) => {
    const params = new URLSearchParams()
    if (memberId) params.append('member_id', memberId)
    if (origin) params.append('origin', origin)
    const query = params.toString()
    return http.get(query ? `/recommendations?${query}` : '/recommendations')
  },
  getOrigins: () => http.get('/recommendations/origins'),
}
