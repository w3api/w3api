---
title: PersistenceService.setTag()
permalink: Java/PersistenceService/setTag
date: 2021-01-11
key: JavaJava.P.PersistenceService
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PersistenceService.metodos valor="setTag" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setTag(URL url, int tag) throws MalformedURLException, IOException
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **int tag**,  {% include w3api/param_description.html metodo=_dato parametro="int tag" %}

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
