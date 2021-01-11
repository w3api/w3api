---
title: DownloadService.removeResource()
permalink: Java/DownloadService/removeResource
date: 2021-01-11
key: JavaJava.D.DownloadService
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DownloadService.metodos valor="removeResource" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void removeResource(URL ref, String version) throws IOException
~~~

## Parámetros
* **URL ref**,  {% include w3api/param_description.html metodo=_dato parametro="URL ref" %}
* **String version**,  {% include w3api/param_description.html metodo=_dato parametro="String version" %}

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
