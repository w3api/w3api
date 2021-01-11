---
title: DownloadServiceListener.upgradingArchive()
permalink: Java/DownloadServiceListener/upgradingArchive
date: 2021-01-11
key: JavaJava.D.DownloadServiceListener
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DownloadServiceListener.metodos valor="upgradingArchive" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void upgradingArchive(URL url, String version, int patchPercent, int overallPercent)
~~~

## Parámetros
* **int overallPercent**,  {% include w3api/param_description.html metodo=_dato parametro="int overallPercent" %}
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **int patchPercent**,  {% include w3api/param_description.html metodo=_dato parametro="int patchPercent" %}
* **String version**,  {% include w3api/param_description.html metodo=_dato parametro="String version" %}

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
