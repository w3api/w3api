---
title: SaslServer
permalink: Java/SaslServer
date: 2021-01-04
key: JavaJava.S.SaslServer
category: java
tags: ['java se', 'javax.security.sasl', 'java.security.sasl', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SaslServer.description }}

## Sintaxis
~~~java
public interface SaslServer
~~~

## Métodos
* [dispose()](/Java/SaslServer/dispose)
* [evaluateResponse()](/Java/SaslServer/evaluateResponse)
* [getAuthorizationID()](/Java/SaslServer/getAuthorizationID)
* [getMechanismName()](/Java/SaslServer/getMechanismName)
* [getNegotiatedProperty()](/Java/SaslServer/getNegotiatedProperty)
* [isComplete()](/Java/SaslServer/isComplete)
* [unwrap()](/Java/SaslServer/unwrap)
* [wrap()](/Java/SaslServer/wrap)

## Ejemplo
~~~java
{{ site.data.Java.S.SaslServer.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SaslServer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
