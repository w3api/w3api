---
title: LinkerServices.getWithLookup()
permalink: Java/LinkerServices/getWithLookup
date: 2021-01-11
key: JavaJava.L.LinkerServices
category: java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkerServices.metodos valor="getWithLookup" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T> T getWithLookup(Supplier<T> operation, SecureLookupSupplier lookupSupplier)
~~~

## Parámetros
* **Supplier&lt;T&gt; operation**,  {% include w3api/param_description.html metodo=_dato parametro="Supplier<T> operation" %}
* **SecureLookupSupplier lookupSupplier**,  {% include w3api/param_description.html metodo=_dato parametro="SecureLookupSupplier lookupSupplier" %}

## Clase Padre
[LinkerServices](/Java/LinkerServices/)

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
