---
title: PersistenceService.create()
permalink: /Java/PersistenceService/create/
date: 2021-01-11
key: Java.P.PersistenceService
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PersistenceService.metodos valor="create" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long create(URL url, long maxsize) throws MalformedURLException, IOException
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **long maxsize**,  {% include w3api/param_description.html metodo=_dato parametro="long maxsize" %}

## Excepciones
[MalformedURLException](/Java/MalformedURLException/), [IOException](/Java/IOException/)

## Clase Padre
[PersistenceService](/Java/PersistenceService/)

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
