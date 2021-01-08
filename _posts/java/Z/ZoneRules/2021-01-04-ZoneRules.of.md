---
title: ZoneRules.of()
permalink: Java/ZoneRules/of
date: 2021-01-04
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
* **ZoneOffset baseWallOffset**,  {% include w3api/param_description.html metodo=_data parametro="ZoneOffset baseWallOffset" %}
* **List&lt;ZoneOffsetTransition&gt; standardOffsetTransitionList**,  {% include w3api/param_description.html metodo=_data parametro="List<ZoneOffsetTransition> standardOffsetTransitionList" %}
* **ZoneOffset offset**,  {% include w3api/param_description.html metodo=_data parametro="ZoneOffset offset" %}
* **List&lt;ZoneOffsetTransition&gt; transitionList**,  {% include w3api/param_description.html metodo=_data parametro="List<ZoneOffsetTransition> transitionList" %}
* **ZoneOffset baseStandardOffset**,  {% include w3api/param_description.html metodo=_data parametro="ZoneOffset baseStandardOffset" %}
* **List&lt;ZoneOffsetTransitionRule&gt; lastRules**,  {% include w3api/param_description.html metodo=_data parametro="List<ZoneOffsetTransitionRule> lastRules" %}

## Clase Padre
[ZoneRules](/Java/ZoneRules/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.Z.ZoneRules.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
