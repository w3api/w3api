---
title: ModifiableObservableListBase.doAdd()
permalink: Java/ModifiableObservableListBase/doAdd
date: 2021-01-11
key: JavaJava.M.ModifiableObservableListBase
category: Java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModifiableObservableListBase.metodos valor="doAdd" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void doAdd(int index, E element)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **E element**,  {% include w3api/param_description.html metodo=_dato parametro="E element" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ModifiableObservableListBase](/Java/ModifiableObservableListBase/)

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
