---
title: SOAPMessage.writeTo()
permalink: /Java/SOAPMessage/writeTo/
date: 2021-01-11
key: Java.S.SOAPMessage
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPMessage.metodos valor="writeTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void writeTo(OutputStream out) throws SOAPException, IOException
~~~

## Parámetros
* **OutputStream out**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream out" %}

## Excepciones
[SOAPException](/Java/SOAPException/), [IOException](/Java/IOException/)

## Clase Padre
[SOAPMessage](/Java/SOAPMessage/)

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
