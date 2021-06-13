---
title: AttachmentUnmarshaller.getAttachmentAsByteArray()
permalink: /Java/AttachmentUnmarshaller/getAttachmentAsByteArray/
date: 2021-01-11
key: Java.A.AttachmentUnmarshaller
category: Java
tags: ['java se', 'javax.xml.bind.attachment', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttachmentUnmarshaller.metodos valor="getAttachmentAsByteArray" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract byte[] getAttachmentAsByteArray(String cid)
~~~

## Parámetros
* **String cid**,  {% include w3api/param_description.html metodo=_dato parametro="String cid" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AttachmentUnmarshaller](/Java/AttachmentUnmarshaller/)

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
