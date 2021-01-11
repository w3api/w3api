---
title: DownloadServiceListener.progress()
permalink: Java/DownloadServiceListener/progress
date: 2021-01-11
key: JavaJava.D.DownloadServiceListener
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DownloadServiceListener.metodos valor="progress" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void progress(URL url, String version, long readSoFar, long total, int overallPercent)
~~~

## Parámetros
* **long readSoFar**,  {% include w3api/param_description.html metodo=_dato parametro="long readSoFar" %}
* **int overallPercent**,  {% include w3api/param_description.html metodo=_dato parametro="int overallPercent" %}
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **String version**,  {% include w3api/param_description.html metodo=_dato parametro="String version" %}
* **long total**,  {% include w3api/param_description.html metodo=_dato parametro="long total" %}

## Clase Padre
[DownloadServiceListener](/Java/DownloadServiceListener/)

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
