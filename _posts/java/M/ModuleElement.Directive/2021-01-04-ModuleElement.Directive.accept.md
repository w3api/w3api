---
title: ModuleElement.Directive.accept()
permalink: Java/ModuleElement/Directive/accept
date: 2021-01-04
key: JavaJava.M.ModuleElement.Directive
category: java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleElement.Directive.metodos valor="accept" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<R,P> R accept(ModuleElement.DirectiveVisitor<R,P> v, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_data parametro="P p" %}
* **P&gt; v**,  {% include w3api/param_description.html metodo=_data parametro="P> v" %}
* **ModuleElement.DirectiveVisitor&lt;R**,  {% include w3api/param_description.html metodo=_data parametro="ModuleElement.DirectiveVisitor<R" %}

## Clase Padre
[ModuleElement.Directive](/Java/ModuleElement/Directive/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ModuleElement.Directive.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
