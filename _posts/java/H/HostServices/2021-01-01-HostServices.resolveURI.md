---
title: HostServices.resolveURI()
permalink: Java/HostServices/resolveURI
date: 2021-01-11
key: JavaJava.H.HostServices
category: java
tags: ['java se', 'javafx.application', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HostServices.metodos valor="resolveURI" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final String resolveURI(String base, String rel)
~~~

## Parámetros
* **String base**,  {% include w3api/param_description.html metodo=_dato parametro="String base" %}
* **String rel**,  {% include w3api/param_description.html metodo=_dato parametro="String rel" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[HostServices](/Java/HostServices/)

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
