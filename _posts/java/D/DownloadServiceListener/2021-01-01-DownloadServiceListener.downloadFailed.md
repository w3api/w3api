---
title: DownloadServiceListener.downloadFailed()
permalink: Java/DownloadServiceListener/downloadFailed
date: 2021-01-11
key: JavaJava.D.DownloadServiceListener
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DownloadServiceListener.metodos valor="downloadFailed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void downloadFailed(URL url, String version)
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
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
