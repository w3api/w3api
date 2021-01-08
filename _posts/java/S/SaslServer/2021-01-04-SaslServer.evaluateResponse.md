---
title: SaslServer.evaluateResponse()
permalink: Java/SaslServer/evaluateResponse
date: 2021-01-04
key: JavaJava.S.SaslServer
category: java
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
* **byte[] response**,  {% include w3api/param_description.html metodo=_data parametro="byte[] response" %}

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
{%- for _ldc in site.data.Java.S.SaslServer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
