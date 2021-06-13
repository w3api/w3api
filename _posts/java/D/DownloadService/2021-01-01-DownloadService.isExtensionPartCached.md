---
title: DownloadService.isExtensionPartCached()
permalink: /Java/DownloadService/isExtensionPartCached/
date: 2021-01-11
key: Java.D.DownloadService
category: Java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DownloadService.metodos valor="isExtensionPartCached" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean isExtensionPartCached(URL ref, String version, String part)
boolean isExtensionPartCached(URL ref, String version, String[] parts)
~~~

## Parámetros
* **String part**,  {% include w3api/param_description.html metodo=_dato parametro="String part" %}
* **String[] parts**,  {% include w3api/param_description.html metodo=_dato parametro="String[] parts" %}
* **URL ref**,  {% include w3api/param_description.html metodo=_dato parametro="URL ref" %}
* **String version**,  {% include w3api/param_description.html metodo=_dato parametro="String version" %}

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
