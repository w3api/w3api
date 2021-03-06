---
title: AttachmentPart.setBase64Content()
permalink: /Java/AttachmentPart/setBase64Content/
date: 2021-01-11
key: Java.A.AttachmentPart
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttachmentPart.metodos valor="setBase64Content" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setBase64Content(InputStream content, String contentType) throws SOAPException
~~~

## Parámetros
* **InputStream content**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream content" %}
* **String contentType**,  {% include w3api/param_description.html metodo=_dato parametro="String contentType" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [SOAPException](/Java/SOAPException/)

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
