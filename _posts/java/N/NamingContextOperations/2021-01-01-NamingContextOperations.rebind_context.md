---
title: NamingContextOperations.rebind_context()
permalink: Java/NamingContextOperations/rebind_context
date: 2021-01-11
key: JavaJava.N.NamingContextOperations
category: Java
tags: ['java se', 'org.omg.CosNaming', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NamingContextOperations.metodos valor="rebind_context" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void rebind_context(NameComponent[] n, NamingContext nc) throws NotFound, CannotProceed, InvalidName
~~~

## Parámetros
* **NamingContext nc**,  {% include w3api/param_description.html metodo=_dato parametro="NamingContext nc" %}
* **NameComponent[] n**,  {% include w3api/param_description.html metodo=_dato parametro="NameComponent[] n" %}

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
