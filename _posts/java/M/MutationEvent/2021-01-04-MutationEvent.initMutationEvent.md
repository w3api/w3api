---
title: MutationEvent.initMutationEvent()
permalink: Java/MutationEvent/initMutationEvent
date: 2021-01-04
key: JavaJava.M.MutationEvent
category: java
tags: ['java se', 'org.w3c.dom.events', 'java.xml', 'metodo java', 'Java 1.5', 'DOM Level 2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MutationEvent.metodos valor="initMutationEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void initMutationEvent(String typeArg, boolean canBubbleArg, boolean cancelableArg, Node relatedNodeArg, String prevValueArg, String newValueArg, String attrNameArg, short attrChangeArg)
~~~

## Parámetros
* **boolean canBubbleArg**,  {% include w3api/param_description.html metodo=_data parametro="boolean canBubbleArg" %}
* **String newValueArg**,  {% include w3api/param_description.html metodo=_data parametro="String newValueArg" %}
* **Node relatedNodeArg**,  {% include w3api/param_description.html metodo=_data parametro="Node relatedNodeArg" %}
* **String typeArg**,  {% include w3api/param_description.html metodo=_data parametro="String typeArg" %}
* **short attrChangeArg**,  {% include w3api/param_description.html metodo=_data parametro="short attrChangeArg" %}
* **String prevValueArg**,  {% include w3api/param_description.html metodo=_data parametro="String prevValueArg" %}
* **boolean cancelableArg**,  {% include w3api/param_description.html metodo=_data parametro="boolean cancelableArg" %}
* **String attrNameArg**,  {% include w3api/param_description.html metodo=_data parametro="String attrNameArg" %}

## Clase Padre
[MutationEvent](/Java/MutationEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MutationEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
