---
title: SaslClient.evaluateChallenge()
permalink: /Java/SaslClient/evaluateChallenge/
date: 2021-01-11
key: Java.S.SaslClient
category: Java
tags: ['java se', 'javax.security.sasl', 'java.security.sasl', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SaslClient.metodos valor="evaluateChallenge" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
byte[] evaluateChallenge(byte[] challenge) throws SaslException
~~~

## Parámetros
* **byte[] challenge**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] challenge" %}

## Excepciones
[SaslException](/Java/SaslException/)

## Clase Padre
[SaslClient](/Java/SaslClient/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
