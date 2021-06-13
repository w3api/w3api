---
title: TextMeasurer.getLayout()
permalink: /Java/TextMeasurer/getLayout/
date: 2021-01-11
key: Java.T.TextMeasurer
category: Java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextMeasurer.metodos valor="getLayout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TextLayout getLayout(int start, int limit)
~~~

## Parámetros
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **int limit**,  {% include w3api/param_description.html metodo=_dato parametro="int limit" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[TextMeasurer](/Java/TextMeasurer/)

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
