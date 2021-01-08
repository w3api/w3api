---
title: SimpleBindings.putAll()
permalink: Java/SimpleBindings/putAll
date: 2021-01-04
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
* **Map&lt;? extends String**,  {% include w3api/param_description.html metodo=_data parametro="Map<? extends String" %}
* **? extends Object&gt; toMerge**,  {% include w3api/param_description.html metodo=_data parametro="? extends Object> toMerge" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SimpleBindings](/Java/SimpleBindings/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SimpleBindings.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
