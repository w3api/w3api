---
title: SOAPMessage.addAttachmentPart()
permalink: /Java/SOAPMessage/addAttachmentPart/
date: 2021-01-11
key: Java.S.SOAPMessage
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPMessage.metodos valor="addAttachmentPart" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void addAttachmentPart(AttachmentPart attachmentPart)
~~~

## Parámetros
* **AttachmentPart attachmentPart**,  {% include w3api/param_description.html metodo=_dato parametro="AttachmentPart attachmentPart" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
