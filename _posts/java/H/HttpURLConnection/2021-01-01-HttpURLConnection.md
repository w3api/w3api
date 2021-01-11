---
title: HttpURLConnection
permalink: Java/HttpURLConnection
date: 2021-01-11
key: JavaJava.H.HttpURLConnection
category: java
tags: ['java se', 'java.net', 'java.base', 'clase java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.H.HttpURLConnection.description }}

## Sintaxis
~~~java
public abstract class HttpURLConnection extends URLConnection
~~~

## Constructores
* [HttpURLConnection()](/Java/HttpURLConnection/HttpURLConnection/)

## Campos
* [chunkLength](/Java/HttpURLConnection/chunkLength)
* [fixedContentLength](/Java/HttpURLConnection/fixedContentLength)
* [fixedContentLengthLong](/Java/HttpURLConnection/fixedContentLengthLong)
* [HTTP_ACCEPTED](/Java/HttpURLConnection/HTTP_ACCEPTED)
* [HTTP_BAD_GATEWAY](/Java/HttpURLConnection/HTTP_BAD_GATEWAY)
* [HTTP_BAD_METHOD](/Java/HttpURLConnection/HTTP_BAD_METHOD)
* [HTTP_BAD_REQUEST](/Java/HttpURLConnection/HTTP_BAD_REQUEST)
* [HTTP_CLIENT_TIMEOUT](/Java/HttpURLConnection/HTTP_CLIENT_TIMEOUT)
* [HTTP_CONFLICT](/Java/HttpURLConnection/HTTP_CONFLICT)
* [HTTP_CREATED](/Java/HttpURLConnection/HTTP_CREATED)
* [HTTP_ENTITY_TOO_LARGE](/Java/HttpURLConnection/HTTP_ENTITY_TOO_LARGE)
* [HTTP_FORBIDDEN](/Java/HttpURLConnection/HTTP_FORBIDDEN)
* [HTTP_GATEWAY_TIMEOUT](/Java/HttpURLConnection/HTTP_GATEWAY_TIMEOUT)
* [HTTP_GONE](/Java/HttpURLConnection/HTTP_GONE)
* [HTTP_INTERNAL_ERROR](/Java/HttpURLConnection/HTTP_INTERNAL_ERROR)
* [HTTP_LENGTH_REQUIRED](/Java/HttpURLConnection/HTTP_LENGTH_REQUIRED)
* [HTTP_MOVED_PERM](/Java/HttpURLConnection/HTTP_MOVED_PERM)
* [HTTP_MOVED_TEMP](/Java/HttpURLConnection/HTTP_MOVED_TEMP)
* [HTTP_MULT_CHOICE](/Java/HttpURLConnection/HTTP_MULT_CHOICE)
* [HTTP_NO_CONTENT](/Java/HttpURLConnection/HTTP_NO_CONTENT)
* [HTTP_NOT_ACCEPTABLE](/Java/HttpURLConnection/HTTP_NOT_ACCEPTABLE)
* [HTTP_NOT_AUTHORITATIVE](/Java/HttpURLConnection/HTTP_NOT_AUTHORITATIVE)
* [HTTP_NOT_FOUND](/Java/HttpURLConnection/HTTP_NOT_FOUND)
* [HTTP_NOT_IMPLEMENTED](/Java/HttpURLConnection/HTTP_NOT_IMPLEMENTED)
* [HTTP_NOT_MODIFIED](/Java/HttpURLConnection/HTTP_NOT_MODIFIED)
* [HTTP_OK](/Java/HttpURLConnection/HTTP_OK)
* [HTTP_PARTIAL](/Java/HttpURLConnection/HTTP_PARTIAL)
* [HTTP_PAYMENT_REQUIRED](/Java/HttpURLConnection/HTTP_PAYMENT_REQUIRED)
* [HTTP_PRECON_FAILED](/Java/HttpURLConnection/HTTP_PRECON_FAILED)
* [HTTP_PROXY_AUTH](/Java/HttpURLConnection/HTTP_PROXY_AUTH)
* [HTTP_REQ_TOO_LONG](/Java/HttpURLConnection/HTTP_REQ_TOO_LONG)
* [HTTP_RESET](/Java/HttpURLConnection/HTTP_RESET)
* [HTTP_SEE_OTHER](/Java/HttpURLConnection/HTTP_SEE_OTHER)
* [HTTP_SERVER_ERROR](/Java/HttpURLConnection/HTTP_SERVER_ERROR)
* [HTTP_UNAUTHORIZED](/Java/HttpURLConnection/HTTP_UNAUTHORIZED)
* [HTTP_UNAVAILABLE](/Java/HttpURLConnection/HTTP_UNAVAILABLE)
* [HTTP_UNSUPPORTED_TYPE](/Java/HttpURLConnection/HTTP_UNSUPPORTED_TYPE)
* [HTTP_USE_PROXY](/Java/HttpURLConnection/HTTP_USE_PROXY)
* [HTTP_VERSION](/Java/HttpURLConnection/HTTP_VERSION)
* [instanceFollowRedirects](/Java/HttpURLConnection/instanceFollowRedirects)
* [method](/Java/HttpURLConnection/method)
* [responseCode](/Java/HttpURLConnection/responseCode)
* [responseMessage](/Java/HttpURLConnection/responseMessage)

## Métodos
* [disconnect()](/Java/HttpURLConnection/disconnect)
* [getErrorStream()](/Java/HttpURLConnection/getErrorStream)
* [getFollowRedirects()](/Java/HttpURLConnection/getFollowRedirects)
* [getHeaderField()](/Java/HttpURLConnection/getHeaderField)
* [getHeaderFieldKey()](/Java/HttpURLConnection/getHeaderFieldKey)
* [getInstanceFollowRedirects()](/Java/HttpURLConnection/getInstanceFollowRedirects)
* [getPermission()](/Java/HttpURLConnection/getPermission)
* [getRequestMethod()](/Java/HttpURLConnection/getRequestMethod)
* [getResponseCode()](/Java/HttpURLConnection/getResponseCode)
* [getResponseMessage()](/Java/HttpURLConnection/getResponseMessage)
* [setAuthenticator()](/Java/HttpURLConnection/setAuthenticator)
* [setChunkedStreamingMode()](/Java/HttpURLConnection/setChunkedStreamingMode)
* [setFixedLengthStreamingMode()](/Java/HttpURLConnection/setFixedLengthStreamingMode)
* [setFollowRedirects()](/Java/HttpURLConnection/setFollowRedirects)
* [setInstanceFollowRedirects()](/Java/HttpURLConnection/setInstanceFollowRedirects)
* [setRequestMethod()](/Java/HttpURLConnection/setRequestMethod)
* [usingProxy()](/Java/HttpURLConnection/usingProxy)

## Ejemplo
~~~java
{{ site.data.Java.H.HttpURLConnection.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpURLConnection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
