---
title: DownloadService.removeExtensionPart()
permalink: Java/DownloadService/removeExtensionPart
date: 2021-01-04
key: JavaJava.D.DownloadService
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DownloadService.metodos valor="removeExtensionPart" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void removeExtensionPart(URL ref, String version, String part) throws IOException
void removeExtensionPart(URL ref, String version, String[] parts) throws IOException
~~~

## Parámetros
* **String version**,  {% include w3api/param_description.html metodo=_data parametro="String version" %}
* **String part**,  {% include w3api/param_description.html metodo=_data parametro="String part" %}
* **URL ref**,  {% include w3api/param_description.html metodo=_data parametro="URL ref" %}
* **String[] parts**,  {% include w3api/param_description.html metodo=_data parametro="String[] parts" %}

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
