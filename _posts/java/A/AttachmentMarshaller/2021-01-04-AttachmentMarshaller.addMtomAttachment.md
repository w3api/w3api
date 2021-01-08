---
title: AttachmentMarshaller.addMtomAttachment()
permalink: Java/AttachmentMarshaller/addMtomAttachment
date: 2021-01-04
key: JavaJava.A.AttachmentMarshaller
category: java
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
* **String elementLocalName**,  {% include w3api/param_description.html metodo=_data parametro="String elementLocalName" %}
* **DataHandler data**,  {% include w3api/param_description.html metodo=_data parametro="DataHandler data" %}
* **byte[] data**,  {% include w3api/param_description.html metodo=_data parametro="byte[] data" %}
* **String elementNamespace**,  {% include w3api/param_description.html metodo=_data parametro="String elementNamespace" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **String mimeType**,  {% include w3api/param_description.html metodo=_data parametro="String mimeType" %}

## Clase Padre
[AttachmentMarshaller](/Java/AttachmentMarshaller/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AttachmentMarshaller.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
