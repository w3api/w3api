---
title: AttachmentPart.setContent()
permalink: Java/AttachmentPart/setContent
date: 2021-01-11
key: JavaJava.A.AttachmentPart
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttachmentPart.metodos valor="setContent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setContent(Object object, String contentType)
~~~

## Parámetros
* **String contentType**,  {% include w3api/param_description.html metodo=_dato parametro="String contentType" %}
* **Object object**,  {% include w3api/param_description.html metodo=_dato parametro="Object object" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
