---
title: AttachmentMarshaller.addMtomAttachment()
permalink: /Java/AttachmentMarshaller/addMtomAttachment/
date: 2021-01-11
key: Java.A.AttachmentMarshaller
category: Java
tags: ['java se', 'javax.xml.bind.attachment', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttachmentMarshaller.metodos valor="addMtomAttachment" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract String addMtomAttachment(byte[] data, int offset, int length, String mimeType, String elementNamespace, String elementLocalName)
public abstract String addMtomAttachment(DataHandler data, String elementNamespace, String elementLocalName)
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **DataHandler data**,  {% include w3api/param_description.html metodo=_dato parametro="DataHandler data" %}
* **String elementLocalName**,  {% include w3api/param_description.html metodo=_dato parametro="String elementLocalName" %}
* **String elementNamespace**,  {% include w3api/param_description.html metodo=_dato parametro="String elementNamespace" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **String mimeType**,  {% include w3api/param_description.html metodo=_dato parametro="String mimeType" %}
* **byte[] data**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] data" %}

## Clase Padre
[AttachmentMarshaller](/Java/AttachmentMarshaller/)

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
