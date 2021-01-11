---
title: SimpleBindings.putAll()
permalink: Java/SimpleBindings/putAll
date: 2021-01-11
key: JavaJava.S.SimpleBindings
category: java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleBindings.metodos valor="putAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void putAll(Map<? extends String,? extends Object> toMerge)
~~~

## Parámetros
* **? extends Object&gt; toMerge**,  {% include w3api/param_description.html metodo=_dato parametro="? extends Object> toMerge" %}
* **Map&lt;? extends String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<? extends String" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SimpleBindings](/Java/SimpleBindings/)

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
