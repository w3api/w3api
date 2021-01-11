---
title: AttachmentPart.setRawContent()
permalink: Java/AttachmentPart/setRawContent
date: 2021-01-11
key: JavaJava.A.AttachmentPart
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttachmentPart.metodos valor="setRawContent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setRawContent(InputStream content, String contentType) throws SOAPException
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
