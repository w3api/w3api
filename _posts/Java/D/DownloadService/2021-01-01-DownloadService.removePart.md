---
title: DownloadService.removePart()
permalink: /Java/DownloadService/removePart/
date: 2021-01-11
key: Java.D.DownloadService
category: Java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DownloadService.metodos valor="removePart" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void removePart(String part) throws IOException
void removePart(String[] parts) throws IOException
~~~

## Parámetros
* **String part**,  {% include w3api/param_description.html metodo=_dato parametro="String part" %}
* **String[] parts**,  {% include w3api/param_description.html metodo=_dato parametro="String[] parts" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[DownloadService](/Java/DownloadService/)

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
