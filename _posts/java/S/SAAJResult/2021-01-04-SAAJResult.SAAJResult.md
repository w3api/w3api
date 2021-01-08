---
title: SAAJResult.SAAJResult()
permalink: Java/SAAJResult/SAAJResult
date: 2021-01-04
key: JavaJava.S.SAAJResult
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6', 'SAAJ Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SAAJResult.constructores valor="SAAJResult" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SAAJResult() throws SOAPException
public SAAJResult(String protocol) throws SOAPException
public SAAJResult(SOAPElement rootNode)
public SAAJResult(SOAPMessage message)
~~~

## Parámetros
* **SOAPElement rootNode**,  {% include w3api/param_description.html metodo=_data parametro="SOAPElement rootNode" %}
* **String protocol**,  {% include w3api/param_description.html metodo=_data parametro="String protocol" %}
* **SOAPMessage message**,  {% include w3api/param_description.html metodo=_data parametro="SOAPMessage message" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[SAAJResult](/Java/SAAJResult/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SAAJResult.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
