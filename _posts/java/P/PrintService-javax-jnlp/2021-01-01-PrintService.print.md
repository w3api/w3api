---
title: PrintService.print()
permalink: Java/PrintService-javax-jnlp/print
date: 2021-01-11
key: JavaJava.P.PrintService-javax-jnlp
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintService-javax-jnlp.metodos valor="print" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean print(Pageable document)
boolean print(Printable painter)
~~~

## Parámetros
* **Printable painter**,  {% include w3api/param_description.html metodo=_dato parametro="Printable painter" %}
* **Pageable document**,  {% include w3api/param_description.html metodo=_dato parametro="Pageable document" %}

## Clase Padre
[PrintService](/Java/PrintService-javax-jnlp/)

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
