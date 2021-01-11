---
title: ZoneRules.of()
permalink: Java/ZoneRules/of
date: 2021-01-11
key: JavaJava.Z.ZoneRules
category: java
tags: ['java se', 'java.time.zone', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZoneRules.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ZoneRules of(ZoneOffset offset)
public static ZoneRules of(ZoneOffset baseStandardOffset, ZoneOffset baseWallOffset, List<ZoneOffsetTransition> standardOffsetTransitionList, List<ZoneOffsetTransition> transitionList, List<ZoneOffsetTransitionRule> lastRules)
~~~

## Parámetros
* **ZoneOffset baseStandardOffset**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneOffset baseStandardOffset" %}
* **ZoneOffset offset**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneOffset offset" %}
* **List&lt;ZoneOffsetTransition&gt; standardOffsetTransitionList**,  {% include w3api/param_description.html metodo=_dato parametro="List<ZoneOffsetTransition> standardOffsetTransitionList" %}
* **List&lt;ZoneOffsetTransitionRule&gt; lastRules**,  {% include w3api/param_description.html metodo=_dato parametro="List<ZoneOffsetTransitionRule> lastRules" %}
* **List&lt;ZoneOffsetTransition&gt; transitionList**,  {% include w3api/param_description.html metodo=_dato parametro="List<ZoneOffsetTransition> transitionList" %}
* **ZoneOffset baseWallOffset**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneOffset baseWallOffset" %}

## Clase Padre
[ZoneRules](/Java/ZoneRules/)

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
