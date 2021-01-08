---
title: AbstractCollection.retainAll()
permalink: Java/AbstractCollection/retainAll
date: 2021-01-04
key: JavaJava.A.AbstractCollection
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractCollection.metodos valor="retainAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean retainAll(Collection<?> c)
~~~

## Parámetros
* **Collection&lt;?&gt; c**,  {% include w3api/param_description.html metodo=_data parametro="Collection<?> c" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AbstractCollection](/Java/AbstractCollection/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractCollection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
