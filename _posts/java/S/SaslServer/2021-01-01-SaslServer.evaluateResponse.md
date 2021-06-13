---
title: SaslServer.evaluateResponse()
permalink: /Java/SaslServer/evaluateResponse/
date: 2021-01-11
key: Java.S.SaslServer
category: Java
tags: ['java se', 'javax.security.sasl', 'java.security.sasl', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SaslServer.metodos valor="evaluateResponse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
byte[] evaluateResponse(byte[] response) throws SaslException
~~~

## Parámetros
* **byte[] response**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] response" %}

## Excepciones
[SaslException](/Java/SaslException/)

## Clase Padre
[SaslServer](/Java/SaslServer/)

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
