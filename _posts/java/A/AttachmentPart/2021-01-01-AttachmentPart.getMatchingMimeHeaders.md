---
title: AttachmentPart.getMatchingMimeHeaders()
permalink: /Java/AttachmentPart/getMatchingMimeHeaders/
date: 2021-01-11
key: Java.A.AttachmentPart
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttachmentPart.metodos valor="getMatchingMimeHeaders" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Iterator<MimeHeader> getMatchingMimeHeaders(String[] names)
~~~

## Parámetros
* **String[] names**,  {% include w3api/param_description.html metodo=_dato parametro="String[] names" %}

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
