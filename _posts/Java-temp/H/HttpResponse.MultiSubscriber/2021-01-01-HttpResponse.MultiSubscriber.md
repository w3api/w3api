---
title: HttpResponse.MultiSubscriber
permalink: /Java/HttpResponse/MultiSubscriber/
date: 2021-01-11
key: Java.H.HttpResponse.MultiSubscriber
category: Java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.H.HttpResponse.MultiSubscriber.description }}

## Sintaxis
~~~java
public static interface HttpResponse.MultiSubscriber<U,T>
~~~

## Métodos
* [asMap()](/Java/HttpResponse/MultiSubscriber/asMap)
* [completion()](/Java/HttpResponse/MultiSubscriber/completion)
* [onError()](/Java/HttpResponse/MultiSubscriber/onError)
* [onPushPromise()](/Java/HttpResponse/MultiSubscriber/onPushPromise)
* [onRequest()](/Java/HttpResponse/MultiSubscriber/onRequest)
* [onResponse()](/Java/HttpResponse/MultiSubscriber/onResponse)

## Ejemplo
~~~java
{{ site.data.Java.H.HttpResponse.MultiSubscriber.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpResponse.MultiSubscriber.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
