---
title: ModuleElement.DirectiveVisitor.visitUnknown()
permalink: Java/ModuleElement/DirectiveVisitor/visitUnknown
date: 2021-01-11
key: JavaJava.M.ModuleElement.DirectiveVisitor
category: java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleElement.DirectiveVisitor.metodos valor="visitUnknown" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default R visitUnknown(ModuleElement.Directive d, P p)
~~~

## Parámetros
* **ModuleElement.Directive d**,  {% include w3api/param_description.html metodo=_dato parametro="ModuleElement.Directive d" %}
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}

## Excepciones
[UnknownDirectiveException](/Java/UnknownDirectiveException/)

## Clase Padre
[ModuleElement.DirectiveVisitor](/Java/ModuleElement/DirectiveVisitor/)

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
