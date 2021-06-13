---
title: SOAPMessage.createAttachmentPart()
permalink: /Java/SOAPMessage/createAttachmentPart/
date: 2021-01-11
key: Java.S.SOAPMessage
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPMessage.metodos valor="createAttachmentPart" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract AttachmentPart createAttachmentPart()
public AttachmentPart createAttachmentPart(Object content, String contentType)
public AttachmentPart createAttachmentPart(DataHandler dataHandler)
~~~

## Parámetros
* **DataHandler dataHandler**,  {% include w3api/param_description.html metodo=_dato parametro="DataHandler dataHandler" %}
* **String contentType**,  {% include w3api/param_description.html metodo=_dato parametro="String contentType" %}
* **Object content**,  {% include w3api/param_description.html metodo=_dato parametro="Object content" %}

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
