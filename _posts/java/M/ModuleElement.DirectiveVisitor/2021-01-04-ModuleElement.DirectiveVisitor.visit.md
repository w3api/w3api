---
title: ModuleElement.DirectiveVisitor.visit()
permalink: Java/ModuleElement/DirectiveVisitor/visit
date: 2021-01-04
key: JavaJava.M.ModuleElement.DirectiveVisitor
category: java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleElement.DirectiveVisitor.metodos valor="visit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default R visit(ModuleElement.Directive d)
default R visit(ModuleElement.Directive d, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_data parametro="P p" %}
* **ModuleElement.Directive d**,  {% include w3api/param_description.html metodo=_data parametro="ModuleElement.Directive d" %}

## Clase Padre
[ModuleElement.DirectiveVisitor](/Java/ModuleElement/DirectiveVisitor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ModuleElement.DirectiveVisitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
