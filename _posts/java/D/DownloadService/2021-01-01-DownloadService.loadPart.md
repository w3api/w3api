---
title: DownloadService.loadPart()
permalink: Java/DownloadService/loadPart
date: 2021-01-11
key: JavaJava.D.DownloadService
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DownloadService.metodos valor="loadPart" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void loadPart(String[] parts, DownloadServiceListener progress) throws IOException
void loadPart(String part, DownloadServiceListener progress) throws IOException
~~~

## Parámetros
* **DownloadServiceListener progress**,  {% include w3api/param_description.html metodo=_dato parametro="DownloadServiceListener progress" %}
* **String[] parts**,  {% include w3api/param_description.html metodo=_dato parametro="String[] parts" %}
* **String part**,  {% include w3api/param_description.html metodo=_dato parametro="String part" %}

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
