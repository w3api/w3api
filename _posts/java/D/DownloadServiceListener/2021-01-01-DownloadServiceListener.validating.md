---
title: DownloadServiceListener.validating()
permalink: Java/DownloadServiceListener/validating
date: 2021-01-11
key: JavaJava.D.DownloadServiceListener
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DownloadServiceListener.metodos valor="validating" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void validating(URL url, String version, long entry, long total, int overallPercent)
~~~

## Parámetros
* **int overallPercent**,  {% include w3api/param_description.html metodo=_dato parametro="int overallPercent" %}
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **long entry**,  {% include w3api/param_description.html metodo=_dato parametro="long entry" %}
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
