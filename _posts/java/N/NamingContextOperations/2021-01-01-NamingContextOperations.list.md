---
title: NamingContextOperations.list()
permalink: Java/NamingContextOperations/list
date: 2021-01-11
key: JavaJava.N.NamingContextOperations
category: Java
tags: ['java se', 'org.omg.CosNaming', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NamingContextOperations.metodos valor="list" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void list(int how_many, BindingListHolder bl, BindingIteratorHolder bi)
~~~

## Parámetros
* **BindingIteratorHolder bi**,  {% include w3api/param_description.html metodo=_dato parametro="BindingIteratorHolder bi" %}
* **BindingListHolder bl**,  {% include w3api/param_description.html metodo=_dato parametro="BindingListHolder bl" %}
* **int how_many**,  {% include w3api/param_description.html metodo=_dato parametro="int how_many" %}

## Clase Padre
[NamingContextOperations](/Java/NamingContextOperations/)

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
