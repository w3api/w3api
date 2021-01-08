---
title: DownloadService.loadResource()
permalink: Java/DownloadService/loadResource
date: 2021-01-04
key: JavaJava.D.DownloadService
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DownloadService.metodos valor="loadResource" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void loadResource(URL ref, String version, DownloadServiceListener progress) throws IOException
~~~

## Parámetros
* **String version**,  {% include w3api/param_description.html metodo=_data parametro="String version" %}
* **URL ref**,  {% include w3api/param_description.html metodo=_data parametro="URL ref" %}
* **DownloadServiceListener progress**,  {% include w3api/param_description.html metodo=_data parametro="DownloadServiceListener progress" %}

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
{%- for _ldc in site.data.Java.D.DownloadService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
