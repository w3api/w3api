---
title: ToolProvider.findFirst()
permalink: /Java/ToolProvider-java-util-spi/findFirst/
date: 2021-01-11
key: Java.T.ToolProvider-java-util-spi
category: Java
tags: ['java se', 'java.util.spi', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ToolProvider-java-util-spi.metodos valor="findFirst" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static Optional<ToolProvider> findFirst(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ToolProvider](/Java/ToolProvider-java-util-spi/)

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
