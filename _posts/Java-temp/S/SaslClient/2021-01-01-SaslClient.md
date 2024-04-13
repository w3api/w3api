---
title: SaslClient
permalink: /Java/SaslClient/
date: 2021-01-11
key: Java.S.SaslClient
category: Java
tags: ['java se', 'javax.security.sasl', 'java.security.sasl', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SaslClient.description }}

## Sintaxis
~~~java
public interface SaslClient
~~~

## Métodos
* [dispose()](/Java/SaslClient/dispose)
* [evaluateChallenge()](/Java/SaslClient/evaluateChallenge)
* [getMechanismName()](/Java/SaslClient/getMechanismName)
* [getNegotiatedProperty()](/Java/SaslClient/getNegotiatedProperty)
* [hasInitialResponse()](/Java/SaslClient/hasInitialResponse)
* [isComplete()](/Java/SaslClient/isComplete)
* [unwrap()](/Java/SaslClient/unwrap)
* [wrap()](/Java/SaslClient/wrap)

## Ejemplo
~~~java
{{ site.data.Java.S.SaslClient.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SaslClient.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
