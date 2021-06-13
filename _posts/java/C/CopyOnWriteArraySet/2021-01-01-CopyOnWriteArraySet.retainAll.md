---
title: CopyOnWriteArraySet.retainAll()
permalink: /Java/CopyOnWriteArraySet/retainAll/
date: 2021-01-11
key: Java.C.CopyOnWriteArraySet
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CopyOnWriteArraySet.metodos valor="retainAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean retainAll(Collection<?> c)
~~~

## Parámetros
* **Collection&lt;?&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<?> c" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CopyOnWriteArraySet](/Java/CopyOnWriteArraySet/)

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
