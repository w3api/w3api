---
title: AttachmentPart.setRawContentBytes()
permalink: Java/AttachmentPart/setRawContentBytes
date: 2021-01-11
key: JavaJava.A.AttachmentPart
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttachmentPart.metodos valor="setRawContentBytes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setRawContentBytes(byte[] content, int offset, int len, String contentType) throws SOAPException
~~~

## Parámetros
* **String contentType**,  {% include w3api/param_description.html metodo=_dato parametro="String contentType" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **byte[] content**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] content" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[AttachmentPart](/Java/AttachmentPart/)

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
