---
title: NamedOperation.NamedOperation()
permalink: /Java/NamedOperation/NamedOperation/
date: 2021-01-11
key: Java.N.NamedOperation
category: Java
tags: ['java se', 'jdk.dynalink', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NamedOperation.constructores valor="NamedOperation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public NamedOperation(Operation baseOperation, Object name)
~~~

## Parámetros
* **Operation baseOperation**,  {% include w3api/param_description.html metodo=_dato parametro="Operation baseOperation" %}
* **Object name**,  {% include w3api/param_description.html metodo=_dato parametro="Object name" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[NamedOperation](/Java/NamedOperation/)

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
