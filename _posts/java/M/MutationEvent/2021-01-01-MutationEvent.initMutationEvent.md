---
title: MutationEvent.initMutationEvent()
permalink: /Java/MutationEvent/initMutationEvent/
date: 2021-01-11
key: Java.M.MutationEvent
category: Java
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
* **String typeArg**,  {% include w3api/param_description.html metodo=_dato parametro="String typeArg" %}
* **String newValueArg**,  {% include w3api/param_description.html metodo=_dato parametro="String newValueArg" %}
* **String prevValueArg**,  {% include w3api/param_description.html metodo=_dato parametro="String prevValueArg" %}
* **Node relatedNodeArg**,  {% include w3api/param_description.html metodo=_dato parametro="Node relatedNodeArg" %}
* **short attrChangeArg**,  {% include w3api/param_description.html metodo=_dato parametro="short attrChangeArg" %}
* **boolean cancelableArg**,  {% include w3api/param_description.html metodo=_dato parametro="boolean cancelableArg" %}
* **String attrNameArg**,  {% include w3api/param_description.html metodo=_dato parametro="String attrNameArg" %}
* **boolean canBubbleArg**,  {% include w3api/param_description.html metodo=_dato parametro="boolean canBubbleArg" %}

## Clase Padre
[MutationEvent](/Java/MutationEvent/)

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
