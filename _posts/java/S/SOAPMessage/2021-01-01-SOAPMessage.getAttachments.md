---
title: SOAPMessage.getAttachments()
permalink: /Java/SOAPMessage/getAttachments/
date: 2021-01-11
key: Java.S.SOAPMessage
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPMessage.metodos valor="getAttachments" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Iterator<AttachmentPart> getAttachments()
public abstract Iterator<AttachmentPart> getAttachments(MimeHeaders headers)
~~~

## Parámetros
* **MimeHeaders headers**,  {% include w3api/param_description.html metodo=_dato parametro="MimeHeaders headers" %}

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
